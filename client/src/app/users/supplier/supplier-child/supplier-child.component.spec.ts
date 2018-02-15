import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SupplierChildComponent } from './supplier-child.component';

describe('SupplierChildComponent', () => {
  let component: SupplierChildComponent;
  let fixture: ComponentFixture<SupplierChildComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SupplierChildComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SupplierChildComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
