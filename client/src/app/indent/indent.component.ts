  import { Inject, Injectable } from '@angular/core';
  import 'rxjs/Rx';
  import { CommonService } from "./../shared/common.service"
  import { Http } from '@angular/http';
  import { Component, OnInit } from '@angular/core';
  import { SESSION_STORAGE, StorageService } from 'angular-webstorage-service';
  import { FormBuilder, FormControl, FormArray, FormGroup } from '@angular/forms';

  @Component({
    selector: 'app-supplier-inventory',
    templateUrl: './indent.component.html',
    styleUrls: ['./indent.component.css']
  })

  @Injectable()
  export class IndentComponent implements OnInit {
    data: any = null;
    endpoint = '/indent/indents/';
    invoiceForm: FormGroup;
    informations = [{
        'tenant': '',
        'buyer': ''
      }];
    indentOrderForm = {};

    constructor(private _fb: FormBuilder, private http: Http, private _service: CommonService, @Inject(SESSION_STORAGE) private storage: StorageService) {
    }

    ngOnInit() {
      this.get_buyer_list();
      this.get_supplier_list();
      this.get_salesman_list();
      this.invoiceForm = this._fb.group({
        itemRows: this._fb.array([this.initItemRows()]) // here
      });
    }

    initItemRows() {
      return this._fb.group({
        // list all your form controls here, which belongs to your form array
        // itemname: [''],
        buyer_name: '',
        seller_name: '',
        bank_name: ''
      });
    }

    addNewRow() {
      // control refers to your formarray
      // const control = <FormArray>this.invoiceForm.controls['itemRows'];
      // add new formgroup
      // control.push(this.initItemRows());

    }

    deleteRow(index: number) {
      // control refers to your formarray
      const control = <FormArray>this.invoiceForm.controls['itemRows'];
      // remove the chosen row
      control.removeAt(index);
    }

    onSubmit = function (my_form: any, my_order_form: any) {
      console.log("indent form value", my_form, my_order_form, this.form);
      this._service.postForm(this.endpoint, my_form)
        .subscribe(
          data => {
            console.log("data posted", data);
          });
    };

    submit_forms = function () {
      let indent_form = document.getElementById('indent_form').onsubmit;
      let order_form = document.getElementById('order_form');
      // let form1 = document.getElementById('order_form').elements;
    };
    get_data = function () {
      // console.log("Get data called tenant" + this.tenant_id);
      // console.log("Local Memory RAHUL: "+ this.storage.get('tenant'));
      this._service.getData(this.endpoint, this.tenant_id)
        .subscribe((response) => {
          console.log("API sent", response);
        });
    };


    get_buyer_list = function () {
      let buyer_endpoint = '/users/buyer/';
      this._service.getData(buyer_endpoint, this.tenant_id)
        .subscribe((response) => {
          console.log("API sent", response);
          this.buyer_list = response;
        });
    };

    get_supplier_list = function () {
      let buyer_endpoint = '/users/supplier/';
      this._service.getData(buyer_endpoint, this.tenant_id)
        .subscribe((response) => {
          console.log("API sent", response);
          this.supplier_list = response;
        });
    };
    get_supplier_child_list = function (selected_buyer: any) {
      console.log("Selected id is : %s", selected_buyer.id);
      // let buyer_endpoint = '/users/supplier/';
      // this._service.getData(buyer_endpoint, this.tenant_id)
      //         .subscribe((response) => {
      //     console.log("API sent", response);
      //     this.supplier_list = response;
      //   });
    };

    get_salesman_list = function () {
      let salesman_endpoint = '/users/salesman/';
      this._service.getData(salesman_endpoint)
        .subscribe((response) => {
          console.log("API sent", response);
          this.salesman_list = response;
        });
    };


    cloneItem = function (event, info) {
      console.log("Info passed is: %s", info);
      let itemToClone = {
        'tenant': info.tenant,
        'buyer': info.buyer
      };
      console.log("event", event.target);
      this.informations.push(itemToClone);
      console.log("New row:", this.informations);
    };

    removeItem = function (itemIndex) {
      console.log("remove :%s", itemIndex);
      this.informations.splice(itemIndex, 1);
    }

  }
