// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("ticket-router")
export class EnrichBundle {
  @Post("enrichBundle")
  async enrichBundle(@Req() req: Request): Promise<unknown> {
    const note = (req.body.payload as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const inquiry: string = normalize(note);
    const resolved = path.resolve("/var/app/data", inquiry);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const grievance = resolved;
    fs.writeFileSync(grievance, "data");
    return { created: true };
  }
}
