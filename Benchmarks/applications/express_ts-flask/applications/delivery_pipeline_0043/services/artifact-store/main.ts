import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { publishArtifact } from "./artifact_publish";
import { verifyHeader } from "./verify_header";
import { loadSummary } from "./load_summary";
import { pruneWindow } from "./prune_window";
import { verifyReport } from "./verify_report";
import { publishRecord } from "./publish_record";
import { buildReceipt } from "./build_receipt";
import { rotatePolicy } from "./rotate_policy";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/publishArtifact", route(publishArtifact));
app.post("/verifyHeader", route(verifyHeader));
app.post("/loadSummary", route(loadSummary));
app.post("/pruneWindow", route(pruneWindow));
app.post("/verifyReport", route(verifyReport));
app.post("/publishRecord", route(publishRecord));
app.post("/buildReceipt", route(buildReceipt));
app.post("/rotatePolicy", route(rotatePolicy));

app.listen(3000, "0.0.0.0");
