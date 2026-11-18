import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { publishArtifact } from "./artifact_publish";
import { formatApproval } from "./format_approval";
import { archiveBatch } from "./archive_batch";
import { publishHeader } from "./publish_header";
import { exportReport } from "./export_report";
import { rotateManifest } from "./rotate_manifest";
import { formatWindow } from "./format_window";
import { pruneHeader } from "./prune_header";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/publishArtifact", route(publishArtifact));
app.post("/formatApproval", route(formatApproval));
app.post("/archiveBatch", route(archiveBatch));
app.post("/publishHeader", route(publishHeader));
app.post("/exportReport", route(exportReport));
app.post("/rotateManifest", route(rotateManifest));
app.post("/formatWindow", route(formatWindow));
app.post("/pruneHeader", route(pruneHeader));

app.listen(3000, "0.0.0.0");
