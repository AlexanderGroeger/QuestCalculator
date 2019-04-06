#ifndef ACTIVEFILEWINDOW_H
#define ACTIVEFILEWINDOW_H

#include <QWidget>

namespace Ui {
class activefilewindow;
}

class activefilewindow : public QWidget
{
    Q_OBJECT

public:
    explicit activefilewindow(QWidget *parent = nullptr);
    ~activefilewindow();

private:
    Ui::activefilewindow *ui;
};

#endif // ACTIVEFILEWINDOW_H
