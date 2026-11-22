import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { storeAttachment } from "./attachment_store";
import { buildMacro } from "./build_macro";
import { rotateBundle } from "./rotate_bundle";
import { fetchTicket } from "./fetch_ticket";
import { exportPolicy } from "./export_policy";
import { publishManifest } from "./publish_manifest";
import { publishHeader } from "./publish_header";
import { formatHeader } from "./format_header";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/storeAttachment", route(storeAttachment));
app.post("/buildMacro/:id", route(buildMacro));
app.post("/rotateBundle", route(rotateBundle));
app.post("/fetchTicket", route(fetchTicket));
app.post("/exportPolicy/:id", route(exportPolicy));
app.post("/publishManifest/:id", route(publishManifest));
app.post("/publishHeader", route(publishHeader));
app.post("/formatHeader", route(formatHeader));

app.listen(3000, "0.0.0.0");
