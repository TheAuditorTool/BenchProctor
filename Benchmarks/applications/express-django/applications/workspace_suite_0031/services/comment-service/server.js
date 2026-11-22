const express = require("express");
const session = require("express-session");
const multer = require("multer");

const postComment = require("./comment_post").postComment;
const reconcileManifest = require("./reconcile_manifest").reconcileManifest;
const reconcileComment = require("./reconcile_comment").reconcileComment;
const compactManifest = require("./compact_manifest").compactManifest;
const loadReceipt = require("./load_receipt").loadReceipt;
const annotateLedger = require("./annotate_ledger").annotateLedger;
const archiveSnapshot = require("./archive_snapshot").archiveSnapshot;
const formatRecord = require("./format_record").formatRecord;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/postComment", postComment);
app.post("/reconcileManifest", reconcileManifest);
app.post("/reconcileComment", reconcileComment);
app.post("/compactManifest", compactManifest);
app.post("/loadReceipt", loadReceipt);
app.post("/annotateLedger", annotateLedger);
app.post("/archiveSnapshot", archiveSnapshot);
app.post("/formatRecord", formatRecord);

app.listen(3000, "0.0.0.0");
