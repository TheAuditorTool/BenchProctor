const express = require("express");
const session = require("express-session");

const trackPresence = require("./presence_track").trackPresence;
const compactSummary = require("./compact_summary").compactSummary;
const normalizeSnapshot = require("./normalize_snapshot").normalizeSnapshot;
const publishSchedule = require("./publish_schedule").publishSchedule;
const publishConfig = require("./publish_config").publishConfig;
const renderCheckpoint = require("./render_checkpoint").renderCheckpoint;
const mergeHeader = require("./merge_header").mergeHeader;
const buildDocument = require("./build_document").buildDocument;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/trackPresence", route(trackPresence));
app.post("/compactSummary", route(compactSummary));
app.post("/normalizeSnapshot/:id", route(normalizeSnapshot));
app.post("/publishSchedule", route(publishSchedule));
app.post("/publishConfig", route(publishConfig));
app.post("/renderCheckpoint", route(renderCheckpoint));
app.post("/mergeHeader", route(mergeHeader));
app.post("/buildDocument", route(buildDocument));

app.listen(3000, "0.0.0.0");
