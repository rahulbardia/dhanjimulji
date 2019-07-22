import 'rxjs/Rx';
import { CommonService } from "./../../../shared/common.service"
import { Http } from '@angular/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";

@Component({
  selector: 'app-supplier-child',
  templateUrl: './supplier-child.component.html',
  styleUrls: ['./supplier-child.component.css']
})
export class SupplierChildComponent implements OnInit {
  data: any = null;
  endpoint = '/users/supplierchild/';
  supplier = null;
  constructor(private http: Http, private _supplierService: CommonService, private route: ActivatedRoute) {
  }


  ngOnInit() {
    this.route.paramMap.subscribe(params => {
    this.supplier = params.get("id");
      console.log("Supplier_id passed is %s", this.supplier);
  })
  }

  onSubmit = function(my_form: any){
        my_form.supplier = this.supplier;
        console.log("supplier child form", my_form);
        this._supplierService.postForm(this.endpoint, my_form)
            .subscribe(
            data => {
              console.log("data posted", data);
            });
  };

  get_data = function(my_form: any){
        this._supplierService.getData(this.endpoint, {'supplier': this.supplier})
            .subscribe((response) => {
        console.log("API sent", response);
      });
  };
}
