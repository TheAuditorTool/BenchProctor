// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("mapping-store")
export class ValidateMapping {
  @Post("validateMapping")
  async validateMapping(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers.referer as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(snippet);
    const handshake: string = readInput();
    fs.writeFileSync("/var/uploads/" + handshake, "data");
    return { created: true };
  }
}
