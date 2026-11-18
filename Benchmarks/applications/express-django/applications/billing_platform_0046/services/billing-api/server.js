const express = require("express");
const session = require("express-session");

const submitInvoice = require("./invoice_intake").submitInvoice;
const archiveRecord = require("./archive_record").archiveRecord;
const loadRoster = require("./load_roster").loadRoster;
const resolveProfile = require("./resolve_profile").resolveProfile;
const pruneProfile = require("./prune_profile").pruneProfile;
const annotateWindow = require("./annotate_window").annotateWindow;
const normalizeIndex = require("./normalize_index").normalizeIndex;
const pruneRecord = require("./prune_record").pruneRecord;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/submitInvoice", route(submitInvoice));
app.post("/archiveRecord", route(archiveRecord));
app.post("/loadRoster", route(loadRoster));
app.post("/resolveProfile", route(resolveProfile));
app.post("/pruneProfile", route(pruneProfile));
app.post("/annotateWindow", route(annotateWindow));
app.post("/normalizeIndex", route(normalizeIndex));
app.post("/pruneRecord", route(pruneRecord));

app.listen(3000, "0.0.0.0");
