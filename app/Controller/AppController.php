<?php

/**
 * Application level Controller
 *
 * This file is application-wide controller file. You can put all
 * application-wide controller-related methods here.
 *
 * PHP 5
 *
 * CakePHP(tm) : Rapid Development Framework (http://cakephp.org)
 * Copyright (c) Cake Software Foundation, Inc. (http://cakefoundation.org)
 *
 * Licensed under The MIT License
 * For full copyright and license information, please see the LICENSE.txt
 * Redistributions of files must retain the above copyright notice.
 *
 * @copyright     Copyright (c) Cake Software Foundation, Inc. (http://cakefoundation.org)
 * @link          http://cakephp.org CakePHP(tm) Project
 * @package       app.Controller
 * @since         CakePHP(tm) v 0.2.9
 * @license       http://www.opensource.org/licenses/mit-license.php MIT License
 */
App::uses('Controller', 'Controller');

/**
 * Application Controller
 *
 * Add your application-wide methods in the class below, your controllers
 * will inherit them.
 *
 * @package		app.Controller
 * @link		http://book.cakephp.org/2.0/en/controllers.html#the-app-controller
 */
class AppController extends Controller
{

    public function beforeFilter()
    {
        parent::beforeFilter();

        // $this->set('dongho_day', $this->dongho_day);
        // $this->set('dongho_type', $this->dongho_type);
        $this->set('form_dk', $this->form_dk);
    }

    public $dongho_type = array(
        'au' => 'Đồng hồ cơ',
        'quz' => 'Đồng hồ pin',
    );

    public $dongho_day = array(
        'da' => 'Dây da',
        'th' => 'Dây thép',
    );

    public $form_dk = array(
        '1' => 'Tư vấn kiểm tra (Trang chủ)',
        '3' => 'Đăng ký học thử (Trang chủ)',
        '2' => 'Tư vấn kiểm tra (Menu đăng ký học thử)',
        '4' => 'Đăng ký học thử (Menu đăng ký học thử)',
        '5' => 'Đăng ký tư vấn (Trang khóa học)',
        '6' => 'Đăng ký khóa học (Landing Page)',
        '7' => 'Đăng ký tư vấn (Landing Page)',
        '8' => 'Kiểm tra trình độ miễn phí (Landing Page)',
        '9' => 'Đăng ký nhận tài liệu IELTS (Lộ trình học / Tài liệu)',
    );


    public $category_fields = array(
        // 'navbar'      => 'Trên cùng',
        // 'home'      => 'Top',
        // 'menu_1'      => 'Tour category',
        // 'menu_2'      => 'Mục tour trang chủ',
        // 'sidebar'      => 'Cột phải',
        // 'footer'    => 'Ch.trang ngang',
        // 'footer_1'  => 'Ch.trang cột 1',
        // 'footer_2'  => 'Ch.trang cột 2',
        // 'footer_3'  => 'Ch.trang cột 3',
        // 'menu_3'  => 'Mobile Flashsale',
        // 'menu_4'  => 'Mobile News',
        // 'footer_4'  => 'Ch.trang cột 4',
        // 'footer_5'  => 'Ch.trang cột 5',
        // 'footer_6'  => 'Ch.trang cột 6',
    );

    public function is_valid_json($str)
    {
        if ($str == '')
            return false;

        json_decode($str);
        return (json_last_error() == JSON_ERROR_NONE);
    }
}
