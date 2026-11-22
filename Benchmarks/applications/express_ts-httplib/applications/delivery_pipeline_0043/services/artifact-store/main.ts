import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { publishArtifact } from "./artifact_publish";
import { verifyHeader } from "./verify_header";
import { loadSummary } from "./load_summary";
import { pruneReport } from "./prune_report";
import { archiveSummary } from "./archive_summary";
import { annotateWindow } from "./annotate_window";
import { compactPolicy } from "./compact_policy";
import { summarizeReport } from "./summarize_report";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/publishArtifact", publishArtifact);
app.post("/verifyHeader", verifyHeader);
app.post("/loadSummary", loadSummary);
app.post("/pruneReport", pruneReport);
app.post("/archiveSummary", archiveSummary);
app.post("/annotateWindow/:id", annotateWindow);
app.post("/compactPolicy/:id", compactPolicy);
app.post("/summarizeReport", summarizeReport);

app.listen(3000, "0.0.0.0");
