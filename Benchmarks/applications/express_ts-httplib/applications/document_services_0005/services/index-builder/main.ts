import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { indexDocument } from "./search_index";
import { annotateReport } from "./annotate_report";
import { buildAttachment } from "./build_attachment";
import { collectReport } from "./collect_report";
import { buildCheckpoint } from "./build_checkpoint";
import { exportWindow } from "./export_window";
import { publishRoster } from "./publish_roster";
import { verifyConfig } from "./verify_config";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/indexDocument", route(indexDocument));
app.post("/annotateReport", route(annotateReport));
app.post("/buildAttachment/:id", route(buildAttachment));
app.post("/collectReport", route(collectReport));
app.post("/buildCheckpoint", route(buildCheckpoint));
app.post("/exportWindow/:id", route(exportWindow));
app.post("/publishRoster", route(publishRoster));
app.post("/verifyConfig", route(verifyConfig));

app.listen(3000, "0.0.0.0");
