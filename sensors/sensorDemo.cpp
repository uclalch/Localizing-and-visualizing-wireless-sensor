#include <olectl.h>
#include <sensorsapi.h>
#include <sensors.h>
#include <stdio.h>
#include <wtypes.h>
#include <iostream>
#include <windows.h> 
#include <string>

#pragma comment(lib, "sensorsapi.lib")
#pragma comment(lib, "PortableDeviceGUIDs.lib")
#pragma comment(lib, "ole32.lib")
#pragma comment(lib, "user32.lib")

class SensorEvent : public ISensorEvents {
public:
	SensorEvent() : mCount(0) {
	}

	// IUnknown interface

	STDMETHODIMP_(ULONG) AddRef() {
		return InterlockedIncrement(&mCount);
	}

	STDMETHODIMP_(ULONG) Release() {
		ULONG count = InterlockedDecrement(&mCount);
		if (!count) {
			delete this;
			return 0;
		}
		return count;
	}

	STDMETHODIMP QueryInterface(REFIID iid, void** ppv) {
		if (iid == IID_IUnknown) {
			*ppv = static_cast<IUnknown*>(this);
		}
		else if (iid == IID_ISensorEvents) {
			*ppv = static_cast<ISensorEvents*>(this);
		}
		else {
			return E_NOINTERFACE;
		}
		AddRef();
		return S_OK;
	}

	// ISensorEvents interface

	STDMETHODIMP OnEvent(ISensor* aSensor, REFGUID aId, IPortableDeviceValues* aData) {
		return S_OK;
	}

	STDMETHODIMP OnLeave(REFSENSOR_ID aId) {
		return S_OK;
	}

	STDMETHODIMP OnStateChanged(ISensor* aSensor, SensorState state) {
		return S_OK;
	}

	STDMETHODIMP OnDataUpdated(ISensor* aSensor, ISensorDataReport* aReport) {
		
		// Common values
		double x, y, z;
		PROPVARIANT var = {};
		std::string url = "curl 127.0.0.1:5000/update?";
		
		// Identify sensor
		SENSOR_TYPE_ID type;
		HRESULT hr = aSensor->GetType(&type);
		
		// Gyroscope
		if (type == SENSOR_TYPE_GYROMETER_3D) {
			hr = aReport->GetSensorValue(SENSOR_DATA_TYPE_ANGULAR_VELOCITY_X_DEGREES_PER_SECOND, &var);
			x = var.dblVal;
			hr = aReport->GetSensorValue(SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Y_DEGREES_PER_SECOND, &var);
			y = var.dblVal;
			hr = aReport->GetSensorValue(SENSOR_DATA_TYPE_ANGULAR_VELOCITY_Z_DEGREES_PER_SECOND, &var);
			z = var.dblVal;
			url +=  "gyr_x=" + std::to_string(x) + "&gyr_y=" + std::to_string(y) +
			       "&gyr_z=" + std::to_string(z);
		}

		// Accelerometer
		else if (type == SENSOR_TYPE_ACCELEROMETER_3D) {
			hr = aReport->GetSensorValue(SENSOR_DATA_TYPE_ACCELERATION_X_G, &var);
			x = var.dblVal;
			hr = aReport->GetSensorValue(SENSOR_DATA_TYPE_ACCELERATION_Y_G, &var);
			y = var.dblVal;
			hr = aReport->GetSensorValue(SENSOR_DATA_TYPE_ACCELERATION_Z_G, &var);
			z = var.dblVal;
			url += "acc_x=" + std::to_string(x) + "&acc_y=" + std::to_string(y) +
				  "&acc_z=" + std::to_string(z);
		}

		// Send readings to server
		if (type == SENSOR_TYPE_GYROMETER_3D || type == SENSOR_TYPE_ACCELEROMETER_3D) {
			WinExec(url.c_str(), 1);
			//std::cout << url << "\n";
		}

		return S_OK;
	}

private:
	ULONG mCount;
};

void sensor(SENSOR_TYPE_ID type)
{
	ISensorManager* manager;
	ISensorCollection* collection;

	if (FAILED(CoCreateInstance(CLSID_SensorManager, NULL, CLSCTX_INPROC_SERVER,
		IID_ISensorManager, (void**)&manager)))
		return;

	if (FAILED(manager->GetSensorsByType(type,				// Sensor Type
		&collection)))
		return;

	ULONG count = 0;
	collection->GetCount(&count);
	if (!count)
		return;

	ISensor* sensor;
	collection->GetAt(0, &sensor);
	if (!sensor)
		return;

	IPortableDeviceValues* values;
	if (SUCCEEDED(CoCreateInstance(CLSID_PortableDeviceValues, NULL,
		CLSCTX_INPROC_SERVER,
		IID_IPortableDeviceValues,
		(void**)&values))) {
		if (SUCCEEDED(values->SetUnsignedIntegerValue(
			SENSOR_PROPERTY_CURRENT_REPORT_INTERVAL,
			100))) {											// Sampling Rate (ms)
			IPortableDeviceValues* returns;
			sensor->SetProperties(values, &returns);
		}
	}

	SensorEvent* event = new SensorEvent();
	ISensorEvents* sensorEvents;
	if (FAILED(event->QueryInterface(IID_ISensorEvents,
		(void**)&sensorEvents))) {
		return;
	}

	sensor->SetEventSink(sensorEvents);
}

int main()
{
	CoInitialize(NULL);

	sensor(SENSOR_TYPE_GYROMETER_3D);
	sensor(SENSOR_TYPE_ACCELEROMETER_3D);

	MSG msg;
	while (true) {
		if (PeekMessage(&msg, NULL, 0, 0, PM_REMOVE)) {
			TranslateMessage(&msg);
			DispatchMessage(&msg);
		}
	}

	CoUninitialize();
	return 0;
}