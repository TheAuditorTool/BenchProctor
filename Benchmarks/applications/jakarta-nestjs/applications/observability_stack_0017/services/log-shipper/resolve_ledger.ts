// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("log-shipper")
export class ResolveLedger {
  @Post("resolveLedger")
  async resolveLedger(@Req() req: Request): Promise<unknown> {
    const note = ((req as any).file?.originalname as string) || "";
    const transform = (v: string): string => v.trim();
    const cohort: string = transform(note);
    fs.unlinkSync("/var/app/data/" + cohort);
    return { created: true };
  }
}
