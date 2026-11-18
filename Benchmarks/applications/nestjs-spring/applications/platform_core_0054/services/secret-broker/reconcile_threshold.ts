// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("secret-broker")
export class ReconcileThreshold {
  @Post("reconcileThreshold")
  async reconcileThreshold(@Req() req: Request): Promise<unknown> {
    const snippet = (req.body.payload as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const persona: string = normalize(snippet);
    const resolved = path.resolve("/var/app/data", persona);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const handshake = resolved;
    fs.writeFileSync(handshake, "data");
    return { created: true };
  }
}
