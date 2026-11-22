const express = require("express");
const session = require("express-session");
const multer = require("multer");

const storeAttachment = require("./attachment_store").storeAttachment;
const buildMacro = require("./build_macro").buildMacro;
const rotateBundle = require("./rotate_bundle").rotateBundle;
const fetchTicket = require("./fetch_ticket").fetchTicket;
const exportPolicy = require("./export_policy").exportPolicy;
const publishManifest = require("./publish_manifest").publishManifest;
const publishHeader = require("./publish_header").publishHeader;
const formatHeader = require("./format_header").formatHeader;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/storeAttachment", route(storeAttachment));
app.post("/buildMacro", route(buildMacro));
app.post("/rotateBundle", route(rotateBundle));
app.post("/fetchTicket", route(fetchTicket));
app.post("/exportPolicy", route(exportPolicy));
app.post("/publishManifest", route(publishManifest));
app.post("/publishHeader", route(publishHeader));
app.post("/formatHeader", route(formatHeader));

app.listen(3000, "0.0.0.0");
