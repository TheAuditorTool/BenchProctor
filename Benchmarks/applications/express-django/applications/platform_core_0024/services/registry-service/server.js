const express = require("express");
const session = require("express-session");

const registerService = require("./service_register").registerService;
const publishSnapshot = require("./publish_snapshot").publishSnapshot;
const loadRecord = require("./load_record").loadRecord;
const resolveBundle = require("./resolve_bundle").resolveBundle;
const rotateRecord = require("./rotate_record").rotateRecord;
const publishCheckpoint = require("./publish_checkpoint").publishCheckpoint;
const collectReport = require("./collect_report").collectReport;
const loadReceipt = require("./load_receipt").loadReceipt;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/registerService", route(registerService));
app.post("/publishSnapshot", route(publishSnapshot));
app.post("/loadRecord", route(loadRecord));
app.post("/resolveBundle", route(resolveBundle));
app.post("/rotateRecord", route(rotateRecord));
app.post("/publishCheckpoint", route(publishCheckpoint));
app.post("/collectReport", route(collectReport));
app.post("/loadReceipt", route(loadReceipt));

app.listen(3000, "0.0.0.0");
