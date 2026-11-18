// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("customs-service")
export class ReconcileCheckpoint {
  @Post("reconcileCheckpoint")
  async reconcileCheckpoint(@Req() req: Request): Promise<unknown> {
    const heading = (req.headers.referer as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(heading);
    const consignment: string = readInput();
    fs.writeFileSync("/var/uploads/" + consignment, "data");
    return { created: true };
  }
}
