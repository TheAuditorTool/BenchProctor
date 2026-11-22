import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { buildManifest } from "./manifest_build";
import { summarizeWindow } from "./summarize_window";
import { fetchCheckpoint } from "./fetch_checkpoint";
import { resolveShipment } from "./resolve_shipment";
import { archiveConfig } from "./archive_config";
import { buildCheckpoint } from "./build_checkpoint";
import { buildBatch } from "./build_batch";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/buildManifest/:id", route(buildManifest));
app.post("/summarizeWindow", route(summarizeWindow));
app.post("/fetchCheckpoint", route(fetchCheckpoint));
app.post("/resolveShipment/:id", route(resolveShipment));
app.post("/archiveConfig/:id", route(archiveConfig));
app.post("/buildCheckpoint", route(buildCheckpoint));
app.post("/buildBatch", route(buildBatch));

app.listen(3000, "0.0.0.0");
