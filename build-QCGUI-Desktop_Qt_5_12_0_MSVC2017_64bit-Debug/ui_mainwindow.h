/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QGridLayout *gridLayout;
    QSpacerItem *horizontalSpacer;
    QLabel *label_2;
    QSpacerItem *verticalSpacer;
    QSpacerItem *horizontalSpacer_5;
    QPushButton *pushButton;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *verticalSpacer_2;
    QPushButton *pushButton_2;
    QSpacerItem *horizontalSpacer_4;
    QSpacerItem *horizontalSpacer_3;
    QPushButton *pushButton_3;
    QSpacerItem *horizontalSpacer_6;
    QLabel *label;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1280, 720);
        MainWindow->setStyleSheet(QString::fromUtf8("background-color: black"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        gridLayout = new QGridLayout(centralWidget);
        gridLayout->setSpacing(6);
        gridLayout->setContentsMargins(11, 11, 11, 11);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer, 0, 1, 1, 1);

        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        QFont font;
        font.setFamily(QString::fromUtf8("Maiandra GD"));
        font.setPointSize(24);
        font.setBold(false);
        font.setWeight(50);
        label_2->setFont(font);
        label_2->setTextFormat(Qt::RichText);
        label_2->setAlignment(Qt::AlignCenter);
        label_2->setWordWrap(false);

        gridLayout->addWidget(label_2, 1, 3, 1, 1);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(verticalSpacer, 5, 3, 1, 1);

        horizontalSpacer_5 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_5, 3, 2, 1, 1);

        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setMinimumSize(QSize(256, 256));
        pushButton->setMaximumSize(QSize(256, 256));
        pushButton->setBaseSize(QSize(0, 0));
        QFont font1;
        font1.setFamily(QString::fromUtf8("AR BLANCA"));
        font1.setPointSize(100);
        pushButton->setFont(font1);
        pushButton->setLayoutDirection(Qt::LeftToRight);
        pushButton->setStyleSheet(QString::fromUtf8("background-color: white"));

        gridLayout->addWidget(pushButton, 3, 3, 1, 1);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_2, 0, 7, 1, 1);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::MinimumExpanding);

        gridLayout->addItem(verticalSpacer_2, 2, 3, 1, 1);

        pushButton_2 = new QPushButton(centralWidget);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        pushButton_2->setMinimumSize(QSize(256, 256));
        pushButton_2->setMaximumSize(QSize(256, 256));
        pushButton_2->setFont(font1);
        pushButton_2->setStyleSheet(QString::fromUtf8("background-color: white;\n"
"rgb (256,256,256)"));

        gridLayout->addWidget(pushButton_2, 3, 1, 1, 1);

        horizontalSpacer_4 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_4, 3, 8, 1, 1);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_3, 3, 0, 1, 1);

        pushButton_3 = new QPushButton(centralWidget);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));
        pushButton_3->setMinimumSize(QSize(256, 256));
        pushButton_3->setMaximumSize(QSize(256, 256));
        pushButton_3->setFont(font1);
        pushButton_3->setStyleSheet(QString::fromUtf8("rgb (256, 256, 256)\n"
"background-color: black"));

        gridLayout->addWidget(pushButton_3, 3, 7, 1, 1);

        horizontalSpacer_6 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(horizontalSpacer_6, 3, 4, 1, 1);

        label = new QLabel(centralWidget);
        label->setObjectName(QString::fromUtf8("label"));
        QFont font2;
        font2.setFamily(QString::fromUtf8("Script MT Bold"));
        font2.setPointSize(48);
        font2.setBold(true);
        font2.setWeight(75);
        label->setFont(font2);
        label->setTextFormat(Qt::RichText);
        label->setAlignment(Qt::AlignCenter);
        label->setWordWrap(false);

        gridLayout->addWidget(label, 0, 2, 1, 3);

        MainWindow->setCentralWidget(centralWidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        label_2->setText(QApplication::translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">File Select</span></p></body></html>", nullptr));
        pushButton->setText(QApplication::translate("MainWindow", "2", nullptr));
        pushButton_2->setText(QApplication::translate("MainWindow", "1", nullptr));
        pushButton_3->setText(QApplication::translate("MainWindow", "3", nullptr));
        label->setText(QApplication::translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Quest Calculator</span></p></body></html>", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
