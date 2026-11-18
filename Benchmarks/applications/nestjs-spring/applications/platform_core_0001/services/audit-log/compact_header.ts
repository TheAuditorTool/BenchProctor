// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("audit-log")
export class CompactHeader {
  @Post("compactHeader")
  async compactHeader(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers.referer as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(tagline);
    const persona: string = readInput();
    fs.writeFileSync("/var/uploads/" + persona, "data");
    return { created: true };
  }
}
