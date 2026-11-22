const express = require("express");
const session = require("express-session");

const storeAttachment = require("./attachment_store").storeAttachment;
const normalizeBatch = require("./normalize_batch").normalizeBatch;
const resolveRecord = require("./resolve_record").resolveRecord;
const fetchBatch = require("./fetch_batch").fetchBatch;
const renderProfile = require("./render_profile").renderProfile;
const fetchCheckpoint = require("./fetch_checkpoint").fetchCheckpoint;
const publishBatch = require("./publish_batch").publishBatch;
const summarizeBundle = require("./summarize_bundle").summarizeBundle;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/storeAttachment", route(storeAttachment));
app.post("/normalizeBatch", route(normalizeBatch));
app.post("/resolveRecord", route(resolveRecord));
app.post("/fetchBatch", route(fetchBatch));
app.post("/renderProfile", route(renderProfile));
app.post("/fetchCheckpoint", route(fetchCheckpoint));
app.post("/publishBatch", route(publishBatch));
app.post("/summarizeBundle", route(summarizeBundle));

app.listen(3000, "0.0.0.0");
