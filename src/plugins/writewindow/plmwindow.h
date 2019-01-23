#ifndef PLMWINDOW_H
#define PLMWINDOW_H

#include <QFocusEvent>
#include <QMainWindow>
#include <QAction>
#include "plmbasewindow.h"


class PLMWindow : public PLMBaseWindow {
    Q_OBJECT

public:

    explicit PLMWindow(QWidget       *parent,
                       const QString& name);
    ~PLMWindow();

public slots:

protected:

    //    void focusInEvent(QFocusEvent *event);

private:

    void setMenuActions();

private slots:

private:

    void setupStatusBar();

private:

    QList<QAction *>actionList;
};

#endif // PLMWINDOW_H
