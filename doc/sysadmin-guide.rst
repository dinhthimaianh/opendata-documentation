==============
Hướng dẫn sysadmin
==============

Hướng dẫn này bao gồm các tính quản trị: quản lý người dùng và bộ dữ liệu.
Người dùng sysadmin có thể truy cập và chỉnh sửa bất kỳ tổ chức nào, xem và 
thay đổi chi tiết người dùng và xóa vĩnh viễn bộ dữ liệu. 

-------------------------
Tùy chỉnh giạo diện
-------------------------

Một số tùy chỉnh đơn giản để tùy chỉnh giao diện của trang web của bạn có 
sẵn thông qua giao diện người dùng, tại ``http://<my-url>/ckan-admin/config/``.

.. image:: /images/Tuy-chinh-giao-dien-sysadmin.png

Tại đây bạn có thể chỉnh sửa như sau:

Tiêu đề trang
    This title is used in the HTML <title> of pages served by CKAN (which may
    be displayed on your browser's title bar). For example if your site title is
    "CKAN Demo", the home page is called "Welcome - CKAN Demo". The site title is
    also used in a few other places, e.g. in the alt-text of the main site logo.

Style
    Choose one of five colour schemes for the default theme.

Site tag line
    This is not used in CKAN's current default themes, but may be used in
    future.

Site tag logo
    A URL for the site logo, used at the head of every page of CKAN.

About
    Text that appears on the "about" page, ``http://<my-ckan-url>/about``. You
    can use `Markdown`_ here. If it is left empty, a standard text describing CKAN
    will appear.

.. _Markdown: http://daringfireball.net/projects/markdown/basics

Intro text
    This text appears prominently on the home page of your site.

Custom CSS
    For simple style changes, you can add CSS code here which will be added to
    the ``<head>`` of every page.

-----------------------------------
Managing organizations and datasets
-----------------------------------

A sysadmin user has full access to user accounts, organizations and datasets.
For example, you have access to every organization as if you were a member of
that organization. Thus most management operations are done in exactly the same
way as in the normal web interface.

For example, to add or delete users to an organization, change a user's role in
the organization, delete the organization or edit its description, etc, visit
the organization's home page. You will see the 'Admin' button as if you were a
member of the organization. You can use this to perform all organization admin
functions. For details, see the :doc:`user-guide`.

Similarly, to edit, update or delete a dataset, go to the dataset page and use
the 'Edit' button. As an admin user you can see all datasets including those
that are private to an organization. They will show up when doing a dataset
search.

Moving a dataset between organizations
======================================

To move a dataset between organizations, visit the dataset's Edit page. Choose
the appropriate entry from the "organization" drop-down list, and press "Save".

.. image:: /images/move_dataset_between_organizations.jpg

-----------------------------
Permanently deleting datasets
-----------------------------

A dataset which has been deleted is not permanently removed from CKAN; it is
simply marked as 'deleted' and will no longer show up in search, etc. The
dataset's URL cannot be re-used for a new dataset.

To permanently delete ("purge") a dataset:

* Navigate to the dataset's "Edit" page, and delete it.
* Visit ``http://<my-ckan-url>/ckan-admin/trash/``.

This page shows all deleted datasets and allows you to delete them permanently.

.. warning::

    This operation cannot be reversed!

.. note::

    At present, it is not possible to purge organizations or groups using the
    web UI. This can only be done with access to the server, by directly deleting
    them from CKAN's database.

--------------
Managing users
--------------

To find a user's profile, go to ``http://<my-ckan-url>/user/``. You can search
for users in the search box provided.

You can search by any part of the user profile, including their e-mail address.
This is useful if, for example, a user has forgotten their user ID. For
non-sysadmin users, the search on this page will only match public parts of the
profile, so they cannot search by e-mail address.

On their user profile, you will see a "Manage" button. CKAN displays the user
settings page. You can delete the user or change any of its settings, including
their username, name and password.

.. image:: /images/manage_users.jpg

.. versionadded:: 2.2
   Previous versions of CKAN didn't allow you to delete users through the
   web interface.
