<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Bücher</h1>
        <hr><br><br>
        <alert :message="message"/>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>
          Buch hinzufügen
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">Titel</th>
            <th scope="col">Autor</th>
            <th scope="col">Gelesen</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(book, index) in books" :key="index">
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>
              <span v-if="book.read">Ja</span>
              <span v-else>Nein</span>
            </td>
            <td>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-warning btn-sm">Aktualisieren</button>
                <button type="button" class="btn btn-danger btn-sm">Löschen</button>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addBookModal"
             id="book-modal"
             title="Buch hinzufügen"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-title-group"
                      label="Titel:"
                      label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addBookForm.title"
                        required
                        placeholder="Titel eingeben"/>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Autor:"
                      label-for="form-author-input">
          <b-form-input id="form-author-input"
                        type="text"
                        v-model="addBookForm.author"
                        required
                        placeholder="Autor eingeben"/>
        </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
            <b-form-checkbox value="true">Gelesen</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Absenden</b-button>
        <b-button type="reset" variant="danger">Zurücksetzen</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './alert-component.vue';

export default {
  name: 'book-component',
  data() {
    return {
      books: [],
      addBookForm: {
        title: '',
        author: '',
        read: [],
      },
      message: '',
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getBooks() {
      const path = `${process.env.VUE_APP_API_URL}/books`;
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addBook(payload) {
      const path = `${process.env.VUE_APP_API_URL}/books`;
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Buch hinzugefügt.';
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      let read = false;
      if (this.addBookForm.read[0]) read = true;
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
