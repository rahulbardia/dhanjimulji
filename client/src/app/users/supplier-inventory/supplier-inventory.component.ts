import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-supplier-inventory',
  templateUrl: './supplier-inventory.component.html',
  styleUrls: ['./supplier-inventory.component.css']
})
export class SupplierInventoryComponent implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  onSubmit = function(my_form: any){
    console.log("Successfully submitted form!", my_form.value);
  };

}
