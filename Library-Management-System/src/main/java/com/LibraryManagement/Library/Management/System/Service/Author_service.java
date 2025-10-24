package com.LibraryManagement.Library.Management.System.Service;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;
import java.util.Set;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.LibraryManagement.Library.Management.System.DTO.AuthorDTO;
import com.LibraryManagement.Library.Management.System.Model.Author;
import com.LibraryManagement.Library.Management.System.Model.Books;
import com.LibraryManagement.Library.Management.System.Repository.Author_dao;
import com.LibraryManagement.Library.Management.System.Repository.Books_dao;

import jakarta.transaction.Transactional;

@Service
@Transactional
public class Author_service {

    @Autowired
    private Author_dao authorDao;

    public AuthorDTO addAuthor(AuthorDTO authorDTO) {
        System.out.println("Received DTO: " + authorDTO);

        Author author = new Author();
        author.setAuthorname(authorDTO.getAuthorname());

        Set<Books> bookSet = authorDTO.getBooks().stream()
                .map(title -> {
                    Books book = new Books();
                    book.setBookTitle(title);
                    book.setStock(10L);
                    book.setAuthors(author);
                    return book;
                })
                .collect(Collectors.toSet());

        author.setBooks(bookSet);

        Author savedAuthor = authorDao.save(author);

        Set<String> savedBookTitles = savedAuthor.getBooks().stream()
                .map(Books::getBookTitle)
                .collect(Collectors.toSet());

        AuthorDTO savedAuthorDTO = new AuthorDTO();
        savedAuthorDTO.setAuthorname(savedAuthor.getAuthorname());
        savedAuthorDTO.setBooks(savedBookTitles);

        return savedAuthorDTO;
    }

    public Set<AuthorDTO> getAllAuthors() {
        return authorDao.findAll()
                .stream()
                .map(author -> {
                    Set<String> bookTitles = author.getBooks()
                            .stream()
                            .map(Books::getBookTitle)
                            .collect(Collectors.toSet());
                    return new AuthorDTO(
                            author.getAuthorname(),
                            bookTitles);
                })
                .collect(Collectors.toSet());
    }

}
