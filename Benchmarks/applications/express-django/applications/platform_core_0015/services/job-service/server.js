const express = require("express");
const session = require("express-session");

const scheduleJob = require("./job_schedule").scheduleJob;
const annotateQuota = require("./annotate_quota").annotateQuota;
const buildBatch = require("./build_batch").buildBatch;
const compactBatch = require("./compact_batch").compactBatch;
const summarizeProfile = require("./summarize_profile").summarizeProfile;
const annotateSchedule = require("./annotate_schedule").annotateSchedule;
const buildIndex = require("./build_index").buildIndex;
const mergeSnapshot = require("./merge_snapshot").mergeSnapshot;

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET || "dev", resave: false, saveUninitialized: true }));

const route = (handler) => (req, res, next) => Promise.resolve(handler(req, res, next)).catch(next);

app.get("/health", (req, res) => res.json({ status: "ok" }));
app.post("/scheduleJob", route(scheduleJob));
app.post("/annotateQuota/:id", route(annotateQuota));
app.post("/buildBatch", route(buildBatch));
app.post("/compactBatch", route(compactBatch));
app.post("/summarizeProfile", route(summarizeProfile));
app.post("/annotateSchedule", route(annotateSchedule));
app.post("/buildIndex", route(buildIndex));
app.post("/mergeSnapshot", route(mergeSnapshot));

app.listen(3000, "0.0.0.0");
