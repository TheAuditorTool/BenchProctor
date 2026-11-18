// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("manifest-builder")
export class AnnotateRoster {
  @Post("annotateRoster")
  async annotateRoster(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body.payload as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const consignment: string = normalize(footnote);
    const resolved = path.resolve("/var/app/data", consignment);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const parcel = resolved;
    fs.writeFileSync(parcel, "data");
    return { created: true };
  }
}
