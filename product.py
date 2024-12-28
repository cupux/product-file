import time
import flet as ft
from base.sidebar import SideBar
from base.topbar import TopBar
from components.cards import CustomDisplayCard
from components.fields import CustomTextField
from db.token import get_user
from utils.colors import (
    customPrimaryColor,
    customBgColor,
    customTextColor,
    customTextHeaderColor,
    customSideBarIconColor,
    customDashboardBG,
    customBorderColor,
)
from db.crud import check_data_exists, connect_to_database, get_data
from db import db_path
from utils.validation import Validation


class ProductList(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()

        self.expand = True
        self.bgcolor = customDashboardBG
        is_user, user = get_user(page.client_storage.get("token"))
        page.is_user = is_user
        page.user = user

        self.sidebar = SideBar(page)
        self.topbar = TopBar(page)

        self.main_content = ft.Column(
            spacing=20,
            controls=[
                self.topbar,
                ft.Container(
                    bgcolor="white",
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.Text(
                                        "Product List",
                                        size=20,
                                        weight=ft.FontWeight.BOLD,
                                        color=customTextColor,
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.ADD_CIRCLE,
                                        icon_color="green",
                                        icon_size=20,
                                        tooltip="Add Product",
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.Divider(
                                color=customTextColor, height=0.4, thickness=0.5
                            ),
                        ]
                    ),
                ),
                ft.Container(
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        expand=True,
                        controls=[
                            ft.Row(
                                controls=[
                                    ft.DataTable(
                                        expand=5,
                                        columns=[
                                            ft.DataColumn(
                                                ft.Text("Product Name", color="black")
                                            ),
                                            ft.DataColumn(
                                                ft.Text("Price", color="black")
                                            ),
                                            ft.DataColumn(
                                                ft.Text("Quantity", color="black")
                                            ),
                                            ft.DataColumn(
                                                ft.Text("Action", color="black")
                                            ),
                                        ],
                                        rows=[
                                            ft.DataRow(
                                                cells = [
                                                    ft.DataCell(
                                                        ft.Text("Clever", color="black")
                                                    ),
                                                    ft.DataCell(
                                                        ft.Text("Clever", color="black")
                                                    ),
                                                    ft.DataCell(
                                                        ft.Text("Clever", color="black")
                                                    ),
                                                    ft.DataCell(
                                                        content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.START,
                                                            controls=[
                                                                ft.IconButton(
                                                                    icon=ft.icons.MODE_EDIT_SHARP,
                                                                    icon_color="blue",
                                                                    icon_size=20,
                                                                    tooltip="Edit Record"
                                                                ),
                                                                ft.IconButton(
                                                                    icon=ft.icons.DELETE_FOREVER_ROUNDED,
                                                                    icon_color="blue",
                                                                    icon_size=20,
                                                                    tooltip="Delete Record"
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ]
                                            )
                                        ]
                                    )
                                ]
                            )
                        ],
                    )
                ),
            ],
        )

        self.content = ft.Row(
            spacing=0,
            controls=[
                self.sidebar,
                ft.Container(expand=True, content=self.main_content),
            ],
        )
