==========
Hướng dẫn người sử dụng
==========

Hướng dẫn sử dụng này bao gồm sử dụng giao diện web, để tổ chức, xuất bản
và tìm dữ liệu.

Một số tính năng UI web liên quan đến quản trị trang web chỉ khả dụng cho 
người dùng có phân quyền là sysadmin và đây là tài liệu trong :doc:`sysadmin-guide`.


Người dùng, tổ chức và ủy quyền
======================================

Bạn có thể tìm kiếm dữ liệu mà không cần đăng nhập. Bạn có thể đăng ký tài khoản 
thành viên và đăng nhập.

Mỗi tập dữ liệu được sở hữu bởi một hoặc nhiều tổ chức. Ví dụ: Website được chính 
phủ sử dụng làm cổng thông tin dữ liệu, thì các tổ chức có thể là các cơ quan chính 
chủ khác nhau, mỗi cơ quan công bố dữ liệu. Mỗi tổ chức có thể có quy trình làm việc 
và ủy quyền riêng, cho phép tổ chức quản lý quy trình xuất bản của riêng mình.

Một quản trị viên của tổ chức có thể thêm người dùng vào tổ chức, với các vai trò khác 
nhau tùy thuộc vào mức độ ủy quyền cần thiết. Là thành viên trong một tổ chức có thể 
tạo một bộ dữ liệu thuộc sở hữu của tổ chức đó. Trong thiết lập mặc định, bộ dữ liệu 
này ban đầu là chế độ riêng tư và chỉ hiện thị cho thành viên khác trong cùng một tổ chức. 
Khi muốn công khai bộ dữ liệu thì yêu cầu một mức ủy quyền cao hơn trong tổ chức để thay đổi chế độ.

Nếu bộ dữ liệu không thuộc sở hữu của bất kỳ tổ chức nào, các bộ dữ liệu như vậy có thể được chỉnh 
sửa bởi bất kỳ người dùng đã đăng nhập vào.


Cách sử dụng
==========================

----------
Đăng ký và đăng nhập
----------

Để tạo ID người dùng, sử dụng link "Đăng ký". Web sẽ yêu cầu như sau:

* *Tên tài khoản* -- Các ký tự được sử dụng là chữ cái, số, và ký tự _ .

* *Họ và tên* -- Sẽ được hiện thị trên hồ sơ của bạn.

* *Thư điện tử* -- Sẽ không hiện thị cho người dùng khác.

* *Mật khẩu* -- Nhập cùng một mật khẩu. Mật khẩu ít nhất có 8 ký tự.

.. image:: /images/dang-ky.PNG

Nếu có vấn đề với bất kỳ trường nào, chúng tôi sẽ cho bạn biết vấn đề và cho phép bạn sửa nó. 
Khi các trường được điền chính xác, chúng tôi sẽ tạo tài khoản người dùng của bạn và tự động đăng nhập.

Tính năng của người xuất bản
=======================

.. _adding_a_new_dataset:

Tạo một bộ dữ liệu mới
--------------------

.. note::
    Bạn phải là thành viên của một tổ chức với vai trò là biên tập viên hoặc quản trị viên của tổ chức 
    để thêm và chỉnh sửa các datsets. Xem phần :ref:`creating_an_organization` dưới đây. 

**Bước 1**. Bạn có thể truy cập "Thêm bộ dữ liệu" với hai cách:

a) Chọn liên kết "Dữ liệu" ở đầu trang. Từ đây, chọn nút "Thêm bộ dữ liệu".

b) Chọn liên kết "Tổ chức" ở đầu trang. Chọn tổ chức sẽ sở hữu tập dữ liệu mới của bạn, chọn  
   nút"Thêm bộ dữ liệu". 
   select the page for the organization that should own your new dataset. Provided
   that you are a member of this organization, you can now select the "Add
   Dataset" button above the search box.

**Bước 2**. Để tạo bộ dữ liệu mới bạn cần cung cấp các thông tin cần thiết sau:

* *Tiêu đề* --  Tiêu đề này sẽ là duy nhất trên toàn web, vì vậy hãy đặt tên tiêu đề ngắn gọn nhưng cụ thể. 
  Ví dụ, "mật độ dân số của Việt Nam theo khu vực" tốt hơn so với "Số liệu dân số".

* *Mô tả* -- Bạn có thể thêm mô tả dài hơn về bộ dữ liệu tại đây, bao gồm thông tin như dữ liệu đến từ đâu 
  và bất kỳ thông tin nào mà mọi người sẽ cần biết khi sử dụng dữ liệu.

* *Thẻ* -- (Tags) Ở đây bạn có thể thêm các thẻ sẽ giúp mọi người tìm thấy dữ liệu và liên kết với các dữ 
  liệu liên quan khác. Ví dụ: "Kinh tế", "giáo dục",...

* *Giấy phép* --  Thông tin giấy phép để mọi người biết cách có thể sử dụng dữ liệu.

* *Tổ chức* - Bạn chỉ được chọn các tổ chức mà bạn là thành viên của tổ chức đó.

* *Hiện thị* --  Có hai chế độ hiện thị "Công khai" và "Riêng tư". Bộ dữ liệu hiện thị chế độ "Công khai" sẽ được
  các thành viên không thuộc trong tổ chức hoặc người xem không có tài khoản xem bộ dữ liệu này. Ngược lại,
  hiện thị chế độ "Riêng tư" chỉ có các thành viên trong tổ chức và quản trị viên xem được bộ dữ liệu này.

.. image:: /images/create-new-dataset.png

.. note:: 
    Theo mặc định, trường bắt buộc duy nhất trên trang này là tiêu đề. Tuy nhiên, bạn nên cung cấp đầy đủ thông tin
    để bộ dữ liệu hoàn thiện. 

**Bước 3**.  Khi bạn đã điền thông tin trên trang này, hãy chọn nút "Tiếp theo: Thêm dữ liệu".

**Bước 4**. Web sẽ hiện thị màn hình "Thêm dữ liệu".

.. image:: /images/create-resource.png

Bạn có thể thêm một hoặc nhiều tài nguyên có chứa dữ liệu cho bộ dữ liệu này. Chọn tải một tệp từ máy tính 
hoặc liên kết cho tài nguyên dữ liệu của bạn hoặc tải dữ liệu lên đám mây.

**Bước 5**. Thêm thông tin khác, ở đây sẽ không yêu cầu thông tin này nhưng bạn nên thêm thông tin này:

* *Tên* -- Tên của tài nguyên này, ví dụ "Giá vàng tháng 01 năm 2011". Các tài nguyên khác nhau trong bộ 
  dữ liệu nên có tên khác nhau.

* *Mô tả* -- Một mô tả ngắn về tài nguyên.

* *Định dạng* -- Định dạng tệp của tài nguyên, ví dụ CSV, XLS, JSON, PDF, v.v.

**Bước 6**. Sau khi hoàn tất các thông tin trên, bạn có thể lưu tài nguyên và tạo thêm một tài nguyên khác bằng 
chọn nút "Lưu & thêm". Nếu bạn muốn kết thúc quá trình thêm tài nguyên, chọn nút "Hoàn tất".

Bạn sẽ có thể tìm thấy tập dữ liệu của mình bằng cách nhập tiêu đề hoặc một số từ có liên quan từ mô tả vào hộp 
tìm kiếm dữ liệu. Để biết thêm thông tin về việc tìm kiếm dữ liệu, hãy xem phần :ref:`finding_data`.

.. _creating_an_organization:

Tạo một tổ chức
------------------------

.. _finding_data:

Tìm kiếm dữ liệu
============
