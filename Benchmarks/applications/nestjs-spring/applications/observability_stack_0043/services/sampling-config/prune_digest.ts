// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("sampling-config")
export class PruneDigest {
  @Post("pruneDigest/:id")
  async pruneDigest(@Req() req: Request): Promise<unknown> {
    const note = (req.params.id as string) || "";
    let gauge;
    try { gauge = JSON.parse(note).value || note; }
    catch (e) { gauge = note; }
    fs.unlinkSync("/var/app/data/" + gauge);
    return { created: true };
  }
}
