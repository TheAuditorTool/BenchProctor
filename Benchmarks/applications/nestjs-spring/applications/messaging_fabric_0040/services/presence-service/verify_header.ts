// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("presence-service")
export class VerifyHeader {
  @Post("verifyHeader")
  async verifyHeader(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.referer as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(preface);
    const bulletin: string = readInput();
    fs.writeFileSync("/var/uploads/" + bulletin, "data");
    return { created: true };
  }
}
