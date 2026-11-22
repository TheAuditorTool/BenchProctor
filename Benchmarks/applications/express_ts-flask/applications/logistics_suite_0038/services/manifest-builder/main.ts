import express, { Request, Response } from "express";
import session from "express-session";

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
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/buildManifest", buildManifest);
app.post("/summarizeWindow", summarizeWindow);
app.post("/fetchCheckpoint", fetchCheckpoint);
app.post("/resolveShipment/:id", resolveShipment);
app.post("/archiveConfig/:id", archiveConfig);
app.post("/buildCheckpoint", buildCheckpoint);
app.post("/buildBatch", buildBatch);

app.listen(3000, "0.0.0.0");
