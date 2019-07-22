import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {FormsModule,FormGroup,ReactiveFormsModule} from "@angular/forms"
import {HttpModule} from "@angular/http"
import {RouterModule} from "@angular/router"
import { StorageServiceModule} from 'angular-webstorage-service';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatFormFieldModule} from '@angular/material/form-field';
import {MatCardModule} from '@angular/material/card';
import {MatInputModule} from '@angular/material';


import { AppComponent } from './app.component';
import { UsersComponent } from './users/users.component';
import { IndentComponent } from './indent/indent.component';
import { BuyerComponent } from './users/buyer/buyer.component';
import { SupplierComponent } from './users/supplier/supplier.component';
import { SupplierInventoryComponent } from './users/supplier-inventory/supplier-inventory.component';
import { SalesmanComponent } from './users/salesman/salesman.component';
import { BuyerChildComponent } from './users/buyer/buyer-child/buyer-child.component';
import { SupplierChildComponent } from './users/supplier/supplier-child/supplier-child.component';
import {CommonService} from "./shared/common.service";
import { LoginComponent } from './login/login.component';
import { NavbarComponent } from './navbar/navbar.component';


@NgModule({
  declarations: [
    AppComponent,
    UsersComponent,
    IndentComponent,
    BuyerComponent,
    SupplierComponent,
    SupplierInventoryComponent,
    SalesmanComponent,
    BuyerChildComponent,
    SupplierChildComponent,
    LoginComponent,
    NavbarComponent
    
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    BrowserAnimationsModule,
    MatToolbarModule,
    ReactiveFormsModule,
    MatCardModule,
    MatInputModule,
    MatFormFieldModule,
    StorageServiceModule,
    RouterModule.forRoot([
      {
        path: 'login',
        component: LoginComponent
      },
      {
        path: 'users',
        component: UsersComponent
      },
      {
        path: 'indent',
        component: IndentComponent
      },
      {
        path: 'users/buyer',
        component: BuyerComponent
      },
      {
        path: 'users/supplier',
        component: SupplierComponent
      },
      {
        path: 'users/supplierinventory',
        component: SupplierInventoryComponent
      },
      {
        path: 'users/salesman',
        component: SalesmanComponent
      },
      {
        path: 'users/buyer/buyerchild/:id',
        component: BuyerChildComponent
      },
      {
        path: 'users/supplier/supplierchild/:id',
        component: SupplierChildComponent
      },
      {
        path:"*",
        component:LoginComponent
      },
      {path:'', redirectTo:'/login', pathMatch:'full'}
    ]),
    // RouterModule.forChild(listLazyRoutes())
  ],
  providers: [CommonService],
  bootstrap: [AppComponent]
})
export class AppModule { }
