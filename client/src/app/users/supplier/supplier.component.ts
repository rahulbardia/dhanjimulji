import 'rxjs/Rx';
import { SupplierService } from "./shared/supplier.service"
import { Http } from '@angular/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-supplier',
  templateUrl: './supplier.component.html',
  styleUrls: ['./supplier.component.css']
})
export class SupplierComponent implements OnInit {
data: any = null;
  constructor(private http: Http, private _service: SupplierService) {

  }

  ngOnInit() {
  }

  onSubmit = function(my_form: any){
        this._service.postForm(my_form)
            .subscribe(
            data => {
              console.log("data posted", data);
            });
  };

  get_data = function(my_form: any){
        this._service.getData(5)
            .subscribe((response) => {
        console.log("API sent", response);
      });
  };
}
