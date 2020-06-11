[
    {
        "id": "9c64d036.a22ae",
        "type": "tab",
        "label": "Flow 1",
        "disabled": false,
        "info": ""
    },
    {
        "id": "f1b2b98d.4ea168",
        "type": "tab",
        "label": "Flow 2",
        "disabled": false,
        "info": ""
    },
    {
        "id": "65ff4984.8c18a8",
        "type": "tab",
        "label": "Flow 3",
        "disabled": false,
        "info": ""
    },
    {
        "id": "30c21384.146b3c",
        "type": "ibmiot",
        "z": "",
        "name": "",
        "keepalive": "120",
        "serverName": "",
        "cleansession": true,
        "appId": "",
        "shared": false
    },
    {
        "id": "a5e6dc1c.8c46f",
        "type": "ui_base",
        "theme": {
            "name": "theme-dark",
            "lightTheme": {
                "default": "#0094CE",
                "baseColor": "#0094CE",
                "baseFont": "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif",
                "edited": true,
                "reset": false
            },
            "darkTheme": {
                "default": "#097479",
                "baseColor": "#ff0000",
                "baseFont": "Lucida Sans Typewriter,Lucida Console,Monaco,monospace",
                "edited": true,
                "reset": false
            },
            "customTheme": {
                "name": "Untitled Theme 1",
                "default": "#4B7930",
                "baseColor": "#4B7930",
                "baseFont": "-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen-Sans,Ubuntu,Cantarell,Helvetica Neue,sans-serif"
            },
            "themeState": {
                "base-color": {
                    "default": "#097479",
                    "value": "#ff0000",
                    "edited": true
                },
                "page-titlebar-backgroundColor": {
                    "value": "#ff0000",
                    "edited": false
                },
                "page-backgroundColor": {
                    "value": "#111111",
                    "edited": false
                },
                "page-sidebar-backgroundColor": {
                    "value": "#ffffff",
                    "edited": false
                },
                "group-textColor": {
                    "value": "#ff4d4d",
                    "edited": false
                },
                "group-borderColor": {
                    "value": "#555555",
                    "edited": false
                },
                "group-backgroundColor": {
                    "value": "#333333",
                    "edited": false
                },
                "widget-textColor": {
                    "value": "#eeeeee",
                    "edited": false
                },
                "widget-backgroundColor": {
                    "value": "#ff0000",
                    "edited": false
                },
                "widget-borderColor": {
                    "value": "#333333",
                    "edited": false
                },
                "base-font": {
                    "value": "Lucida Sans Typewriter,Lucida Console,Monaco,monospace"
                }
            },
            "angularTheme": {
                "primary": "indigo",
                "accents": "blue",
                "warn": "red",
                "background": "grey"
            }
        },
        "site": {
            "name": "Node-RED Dashboard",
            "hideToolbar": "false",
            "allowSwipe": "false",
            "lockMenu": "false",
            "allowTempTheme": "true",
            "dateFormat": "DD/MM/YYYY",
            "sizes": {
                "sx": 48,
                "sy": 48,
                "gx": 6,
                "gy": 6,
                "cx": 6,
                "cy": 6,
                "px": 0,
                "py": 0
            }
        }
    },
    {
        "id": "f1ded769.667e58",
        "type": "ui_tab",
        "z": "",
        "name": "Smart Agriculture",
        "icon": "dashboard",
        "disabled": false,
        "hidden": false
    },
    {
        "id": "f3a1c95e.01f1d8",
        "type": "ui_group",
        "z": "",
        "name": "TEMPERATURE",
        "tab": "f1ded769.667e58",
        "order": 1,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "d749a197.45187",
        "type": "ui_group",
        "z": "",
        "name": "OBJECT TEMPERATURE",
        "tab": "f1ded769.667e58",
        "order": 2,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "a8d1c8a9.1ba428",
        "type": "ui_group",
        "z": "",
        "name": "HUMIDITY",
        "tab": "f1ded769.667e58",
        "order": 3,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "70bfc18c.aa1e8",
        "type": "ui_group",
        "z": "",
        "name": "Motor Control",
        "tab": "f1ded769.667e58",
        "order": 4,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "a4895a01.ccdc68",
        "type": "ui_group",
        "z": "",
        "name": "Motor Control",
        "tab": "f1ded769.667e58",
        "order": 5,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "425fe5fc.ee60dc",
        "type": "ui_group",
        "z": "",
        "name": "Weather Condition Details ",
        "tab": "f1ded769.667e58",
        "order": 6,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "90d53c3b.d4953",
        "type": "ui_group",
        "z": "",
        "name": "Weather Condition Details (Others)",
        "tab": "f1ded769.667e58",
        "order": 7,
        "disp": true,
        "width": "6",
        "collapse": false
    },
    {
        "id": "35e780f7.a1f03",
        "type": "ibmiot in",
        "z": "9c64d036.a22ae",
        "authentication": "apiKey",
        "apiKey": "30c21384.146b3c",
        "inputType": "evt",
        "logicalInterface": "",
        "ruleId": "",
        "deviceId": "NodeMCU",
        "applicationId": "",
        "deviceType": "Smart_agriculture",
        "eventType": "iotsensor",
        "commandType": "data",
        "format": "json",
        "name": "IBM IoT",
        "service": "registered",
        "allDevices": "",
        "allApplications": "",
        "allDeviceTypes": "",
        "allLogicalInterfaces": "",
        "allEvents": "",
        "allCommands": "",
        "allFormats": "",
        "qos": 0,
        "x": 130,
        "y": 140,
        "wires": [
            [
                "d69cf614.8e44e8",
                "905c86c8.c69178",
                "92038ca8.4b77",
                "7e02bd5b.1da8a4"
            ]
        ]
    },
    {
        "id": "d69cf614.8e44e8",
        "type": "debug",
        "z": "9c64d036.a22ae",
        "name": "",
        "active": false,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "x": 450,
        "y": 140,
        "wires": []
    },
    {
        "id": "905c86c8.c69178",
        "type": "function",
        "z": "9c64d036.a22ae",
        "name": "Temperature",
        "func": "msg.payload=msg.payload.d.temperature\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 270,
        "y": 22,
        "wires": [
            [
                "d69cf614.8e44e8",
                "2d3178d7.e03098"
            ]
        ]
    },
    {
        "id": "92038ca8.4b77",
        "type": "function",
        "z": "9c64d036.a22ae",
        "name": "Humidity",
        "func": "msg.payload=msg.payload.d.humidity\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 260,
        "y": 240,
        "wires": [
            [
                "d69cf614.8e44e8",
                "1dfddbf2.f1f8d4"
            ]
        ]
    },
    {
        "id": "38c10590.a1b9ea",
        "type": "ibmiot out",
        "z": "9c64d036.a22ae",
        "authentication": "apiKey",
        "apiKey": "30c21384.146b3c",
        "outputType": "cmd",
        "deviceId": "motor",
        "deviceType": "Smart_agriculture",
        "eventCommandType": "command",
        "format": "json",
        "data": "data",
        "qos": 0,
        "name": "IBM IoT",
        "service": "registered",
        "x": 620,
        "y": 320,
        "wires": []
    },
    {
        "id": "1daf8251.c43a4e",
        "type": "inject",
        "z": "9c64d036.a22ae",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "x": 240,
        "y": 620,
        "wires": [
            [
                "b5d7cdfc.31593"
            ]
        ]
    },
    {
        "id": "b5d7cdfc.31593",
        "type": "http request",
        "z": "9c64d036.a22ae",
        "name": "",
        "method": "GET",
        "ret": "obj",
        "paytoqs": false,
        "url": "api.openweathermap.org/data/2.5/weather?q=Hyderabad,IN&units=metric&appid=9cdec2e2eb244a9275671f01b03d2e34",
        "tls": "",
        "persist": false,
        "proxy": "",
        "authType": "",
        "x": 410,
        "y": 620,
        "wires": [
            [
                "7090fbf0.03e954",
                "95c81483.431398",
                "60ec2320.a7bb4c",
                "13a6f8b1.7ab1b7",
                "97d186f4.0ce418",
                "c4b63cbb.1f071",
                "7d95078.72586f8",
                "bb708dcd.bd30f",
                "935017e7.d55f48",
                "d60f51ba.8ed2b"
            ]
        ]
    },
    {
        "id": "7090fbf0.03e954",
        "type": "debug",
        "z": "9c64d036.a22ae",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "x": 610,
        "y": 460,
        "wires": []
    },
    {
        "id": "95c81483.431398",
        "type": "function",
        "z": "9c64d036.a22ae",
        "name": "temp",
        "func": "msg.payload=msg.payload.main.temp\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 610,
        "y": 500,
        "wires": [
            [
                "c2f949d3.68f4e8"
            ]
        ]
    },
    {
        "id": "60ec2320.a7bb4c",
        "type": "function",
        "z": "9c64d036.a22ae",
        "name": "humidity%",
        "func": "msg.payload=msg.payload.main.humidity\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 630,
        "y": 540,
        "wires": [
            [
                "6e8743a0.d67f5c"
            ]
        ]
    },
    {
        "id": "97cb0530.d5cf48",
        "type": "ui_button",
        "z": "9c64d036.a22ae",
        "name": "",
        "group": "a4895a01.ccdc68",
        "order": 1,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "MOTOR OFF",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "{\"command\":\"motoroff\"}",
        "payloadType": "str",
        "topic": "",
        "x": 440,
        "y": 360,
        "wires": [
            [
                "38c10590.a1b9ea"
            ]
        ]
    },
    {
        "id": "c2f949d3.68f4e8",
        "type": "ui_text",
        "z": "9c64d036.a22ae",
        "group": "425fe5fc.ee60dc",
        "order": 0,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "<font color={{msg.red}}>Temperature</font>",
        "format": "<font color={{msg.blue}}>{{msg.payload}}</font>",
        "layout": "row-spread",
        "x": 790,
        "y": 500,
        "wires": []
    },
    {
        "id": "6e8743a0.d67f5c",
        "type": "ui_text",
        "z": "9c64d036.a22ae",
        "group": "425fe5fc.ee60dc",
        "order": 1,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Humidity",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 800,
        "y": 540,
        "wires": []
    },
    {
        "id": "80cb4b24.a0e3e8",
        "type": "ui_text",
        "z": "9c64d036.a22ae",
        "group": "425fe5fc.ee60dc",
        "order": 2,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Weather report",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 820,
        "y": 580,
        "wires": []
    },
    {
        "id": "b644a2b0.5b75c",
        "type": "ui_text",
        "z": "9c64d036.a22ae",
        "group": "425fe5fc.ee60dc",
        "order": 3,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Pressure",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 820,
        "y": 620,
        "wires": []
    },
    {
        "id": "13a6f8b1.7ab1b7",
        "type": "function",
        "z": "9c64d036.a22ae",
        "name": "main",
        "func": "msg.payload=msg.payload.weather[0].main\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 630,
        "y": 580,
        "wires": [
            [
                "80cb4b24.a0e3e8"
            ]
        ]
    },
    {
        "id": "97d186f4.0ce418",
        "type": "function",
        "z": "9c64d036.a22ae",
        "name": "pressure",
        "func": "msg.payload=msg.payload.main.pressure\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 640,
        "y": 620,
        "wires": [
            [
                "b644a2b0.5b75c"
            ]
        ]
    },
    {
        "id": "9e2b67be.f516e8",
        "type": "ui_button",
        "z": "9c64d036.a22ae",
        "name": "",
        "group": "70bfc18c.aa1e8",
        "order": 4,
        "width": 0,
        "height": 0,
        "passthru": false,
        "label": "MOTOR ON",
        "tooltip": "",
        "color": "",
        "bgcolor": "",
        "icon": "",
        "payload": "{\"command\":\"motoron\"}",
        "payloadType": "json",
        "topic": "",
        "x": 440,
        "y": 300,
        "wires": [
            [
                "38c10590.a1b9ea"
            ]
        ]
    },
    {
        "id": "7e02bd5b.1da8a4",
        "type": "function",
        "z": "9c64d036.a22ae",
        "name": "Object temp",
        "func": "msg.payload=msg.payload.d.objectTemp\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 270,
        "y": 60,
        "wires": [
            [
                "d69cf614.8e44e8",
                "69307363.1d089c"
            ]
        ]
    },
    {
        "id": "2d3178d7.e03098",
        "type": "ui_gauge",
        "z": "9c64d036.a22ae",
        "name": "",
        "group": "f3a1c95e.01f1d8",
        "order": 0,
        "width": 0,
        "height": 0,
        "gtype": "gage",
        "title": "TEMPERATURE",
        "label": "Celcius",
        "format": "{{value}}",
        "min": 0,
        "max": "100",
        "colors": [
            "#f5f5f5",
            "#e6e600",
            "#603acb"
        ],
        "seg1": "",
        "seg2": "",
        "x": 710,
        "y": 20,
        "wires": []
    },
    {
        "id": "69307363.1d089c",
        "type": "ui_gauge",
        "z": "9c64d036.a22ae",
        "name": "",
        "group": "d749a197.45187",
        "order": 0,
        "width": 0,
        "height": 0,
        "gtype": "gage",
        "title": "OBJECT TEMPERATURE",
        "label": "Celcius",
        "format": "{{value}}",
        "min": 0,
        "max": "100",
        "colors": [
            "#00b500",
            "#e6e600",
            "#ca3838"
        ],
        "seg1": "",
        "seg2": "",
        "x": 730,
        "y": 60,
        "wires": []
    },
    {
        "id": "1dfddbf2.f1f8d4",
        "type": "ui_gauge",
        "z": "9c64d036.a22ae",
        "name": "",
        "group": "a8d1c8a9.1ba428",
        "order": 0,
        "width": 0,
        "height": 0,
        "gtype": "gage",
        "title": "HUMIDITY",
        "label": "%",
        "format": "{{value}}",
        "min": 0,
        "max": "100",
        "colors": [
            "#00b500",
            "#e6e600",
            "#7e3a3a"
        ],
        "seg1": "",
        "seg2": "",
        "x": 770,
        "y": 240,
        "wires": []
    },
    {
        "id": "c4b63cbb.1f071",
        "type": "function",
        "z": "9c64d036.a22ae",
        "name": "City name",
        "func": "msg.payload=msg.payload.name\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 640,
        "y": 660,
        "wires": [
            [
                "c376c2c8.03f9f"
            ]
        ]
    },
    {
        "id": "7d95078.72586f8",
        "type": "function",
        "z": "9c64d036.a22ae",
        "name": "wind speed",
        "func": "msg.payload=msg.payload.wind.speed\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 650,
        "y": 700,
        "wires": [
            [
                "322e6622.ae520a"
            ]
        ]
    },
    {
        "id": "bb708dcd.bd30f",
        "type": "function",
        "z": "9c64d036.a22ae",
        "name": "wind degree",
        "func": "msg.payload=msg.payload.wind.deg\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 650,
        "y": 740,
        "wires": [
            [
                "443406d6.8d3b28"
            ]
        ]
    },
    {
        "id": "935017e7.d55f48",
        "type": "function",
        "z": "9c64d036.a22ae",
        "name": "Longitude",
        "func": "msg.payload=msg.payload.coord.lon;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 640,
        "y": 780,
        "wires": [
            [
                "3fc95694.66519a"
            ]
        ]
    },
    {
        "id": "d60f51ba.8ed2b",
        "type": "function",
        "z": "9c64d036.a22ae",
        "name": "latitude",
        "func": "msg.payload=msg.payload.coord.lat\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 640,
        "y": 820,
        "wires": [
            [
                "d0c9dd65.628b2"
            ]
        ]
    },
    {
        "id": "c376c2c8.03f9f",
        "type": "ui_text",
        "z": "9c64d036.a22ae",
        "group": "425fe5fc.ee60dc",
        "order": 4,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "City Name",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 830,
        "y": 660,
        "wires": []
    },
    {
        "id": "322e6622.ae520a",
        "type": "ui_text",
        "z": "9c64d036.a22ae",
        "group": "90d53c3b.d4953",
        "order": 0,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Wind Speed",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 830,
        "y": 700,
        "wires": []
    },
    {
        "id": "443406d6.8d3b28",
        "type": "ui_text",
        "z": "9c64d036.a22ae",
        "group": "90d53c3b.d4953",
        "order": 1,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Wind Degree",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 850,
        "y": 740,
        "wires": []
    },
    {
        "id": "3fc95694.66519a",
        "type": "ui_text",
        "z": "9c64d036.a22ae",
        "group": "90d53c3b.d4953",
        "order": 2,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Longitude",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 840,
        "y": 780,
        "wires": []
    },
    {
        "id": "d0c9dd65.628b2",
        "type": "ui_text",
        "z": "9c64d036.a22ae",
        "group": "90d53c3b.d4953",
        "order": 3,
        "width": 0,
        "height": 0,
        "name": "",
        "label": "Latitude",
        "format": "{{msg.payload}}",
        "layout": "row-spread",
        "x": 820,
        "y": 820,
        "wires": []
    }
]