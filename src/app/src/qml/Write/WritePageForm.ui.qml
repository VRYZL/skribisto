import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import ".."

Item {
    id: base
    width: 1000
    height: 600
    property alias rightPaneScrollMouseArea: rightPaneScrollMouseArea
    property alias rightPaneScrollTouchArea: rightPaneScrollTouchArea
    property alias compactHeaderPane: compactHeaderPane
    property alias compactRightDockShowButton: compactRightDockShowButton
    property alias compactLeftDockShowButton: compactLeftDockShowButton
    property alias leftDockMenuGroup: leftDockMenuGroup
    property alias rightDockMenuGroup: rightDockMenuGroup
    property alias leftDockResizeButton: leftDockResizeButton
    property alias rightDockResizeButton: rightDockResizeButton
    property alias leftDockMenuButton: leftDockMenuButton
    property alias rightDockMenuButton: rightDockMenuButton
    property alias leftDock: leftDock
    property alias rightDock: rightDock
    property alias leftDockShowButton: leftDockShowButton
    property alias rightDockShowButton: rightDockShowButton
    property alias minimap: minimap
    property alias middleBase: middleBase
    property alias writingZone: writingZone
    property alias base: base
    property alias leftPaneScrollMouseArea: leftPaneScrollMouseArea
    property alias leftPaneScrollTouchArea: leftPaneScrollTouchArea

    ColumnLayout {
        id: columnLayout
        spacing: 0
        anchors.fill: parent

        Pane {
            id: compactHeaderPane
            width: 200
            height: 200
            padding: 2
            Layout.fillHeight: false
            Layout.preferredHeight: 50
            Layout.fillWidth: true

            RowLayout {
                id: rowLayout1
                spacing: 2
                anchors.fill: parent
                RowLayout {
                    id: rowLayout2
                    spacing: 2
                    Layout.alignment: Qt.AlignLeft | Qt.AlignTop
                    Button {
                        id: compactLeftDockShowButton
                        Layout.preferredHeight: 50
                        Layout.preferredWidth: 50
                        flat: true
                        Layout.alignment: Qt.AlignLeft | Qt.AlignTop
                    }
                }
                RowLayout {
                    id: rowLayout3
                    spacing: 2
                    Layout.alignment: Qt.AlignRight | Qt.AlignTop
                    Button {
                        id: compactRightDockShowButton
                        Layout.preferredHeight: 50
                        Layout.preferredWidth: 50
                        flat: true
                        Layout.alignment: Qt.AlignRight | Qt.AlignTop
                    }
                }
            }
        }

        RowLayout {
            id: rowLayout
            Layout.fillHeight: true
            Layout.fillWidth: true
            spacing: 0

            Item {
                id: leftBase
                Layout.minimumWidth: 400
                visible: !Globals.compactSize
                Layout.fillHeight: true
                Layout.preferredWidth: Globals.compactSize ? -1 : base.width / 6
                z: 1

                RowLayout {
                    anchors.fill: parent

                    WriteLeftDock {
                        id: leftDock
                        Layout.fillHeight: true
                    }

                    Pane{
                        id: leftPane
                        Layout.fillHeight: true
                        Layout.fillWidth: true

                        MultiPointTouchArea {
                            id: leftPaneScrollTouchArea
                            z: 1
                            anchors.fill: parent
                            mouseEnabled: false
                            maximumTouchPoints: 1
                            touchPoints: [
                                TouchPoint {
                                    id: leftTouch1
                                }
                            ]
                        }

                        MouseArea {
                            id: leftPaneScrollMouseArea
                            z: 0
                            anchors.fill: parent
                        }

                        ColumnLayout {
                            anchors.fill: parent
                            Button {
                                id: leftDockShowButton
                                focusPolicy: Qt.NoFocus
                                Layout.preferredHeight: 50
                                Layout.preferredWidth: 50
                                flat: true
                                Layout.alignment: Qt.AlignLeft | Qt.AlignTop
                            }

                            Button {
                                id: leftDockMenuButton
                                focusPolicy: Qt.NoFocus
                                checkable: true
                                Layout.preferredHeight: 50
                                Layout.preferredWidth: 50
                                flat: true
                                Layout.alignment: Qt.AlignLeft | Qt.AlignTop
                            }

                            ColumnLayout {
                                id: leftDockMenuGroup
                                Layout.alignment: Qt.AlignLeft | Qt.AlignTop

                                Button {
                                    id: leftDockResizeButton
                                    focusPolicy: Qt.NoFocus
                                    Layout.preferredHeight: 50
                                    Layout.preferredWidth: 50
                                    flat: true
                                    Layout.alignment: Qt.AlignLeft | Qt.AlignTop
                                }
                            }
                        }
                    }


                }
            }

            Item {
                id: middleBase
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.fillHeight: true
                Layout.fillWidth: true

                WritingZone {
                    id: writingZone
                    anchors.fill: parent
                }
            }

            Item {
                id: rightBase
                Layout.minimumWidth: 400
                visible: !Globals.compactSize
                Layout.fillHeight: true
                Layout.preferredWidth: Globals.compactSize ? -1 : base.width / 6
                z: 1

                RowLayout {
                    anchors.fill: parent


                    Pane{
                        id: rightPane
                        Layout.fillHeight: true
                        Layout.fillWidth: true

                        MultiPointTouchArea {
                            id: rightPaneScrollTouchArea
                            z: 1
                            anchors.fill: parent
                            mouseEnabled: false
                            maximumTouchPoints: 1
                            touchPoints: [
                                TouchPoint {
                                    id: leftTouch2
                                }
                            ]
                        }

                        MouseArea {
                            id: rightPaneScrollMouseArea
                            z: 0
                            anchors.fill: parent
                        }

                        ColumnLayout {

                            anchors.fill: parent
                            Button {
                                id: rightDockShowButton
                                focusPolicy: Qt.NoFocus
                                Layout.preferredHeight: 50
                                Layout.preferredWidth: 50
                                flat: true
                                Layout.alignment: Qt.AlignRight | Qt.AlignTop
                            }

                            Button {
                                id: rightDockMenuButton
                                focusPolicy: Qt.NoFocus
                                checkable: true
                                Layout.preferredHeight: 50
                                Layout.preferredWidth: 50
                                flat: true
                                Layout.alignment: Qt.AlignRight | Qt.AlignTop
                            }

                            ColumnLayout {
                                id: rightDockMenuGroup
                                Layout.alignment: Qt.AlignRight | Qt.AlignTop

                                Button {
                                    id: rightDockResizeButton
                                    focusPolicy: Qt.NoFocus
                                    Layout.preferredHeight: 50
                                    Layout.preferredWidth: 50
                                    flat: true
                                    Layout.alignment: Qt.AlignRight | Qt.AlignTop
                                }
                            }
                        }
                    }
                    Minimap {
                        Layout.fillHeight: true
                        Layout.alignment: Qt.AlignRight | Qt.AlignVCenter

                        id: minimap
                        //width: minimapFlickable.width
                        //pageSize: (writingZone.flickable.height) / (writingZone.textArea.contentHeight + 16)
                        //textScale: minimapFlickable.height / writingZone.flickable.contentHeight
                        sourceWidth: writingZone.textArea.width
                        sourcePointSize: writingZone.textArea.font.pointSize
                    }
                    WriteRightDock {
                        id: rightDock
                        Layout.fillHeight: true
                    }

                }
            }
        }
    }
}

/*##^##
Designer {
    D{i:0;width:1200}D{i:17;anchors_height:100;anchors_width:100}D{i:21;anchors_height:100;anchors_width:100}
}
##^##*/

