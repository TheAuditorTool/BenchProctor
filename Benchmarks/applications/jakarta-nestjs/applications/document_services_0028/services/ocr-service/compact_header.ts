// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("ocr-service")
export class CompactHeader {
  @Post("compactHeader")
  async compactHeader(@Req() req: Request): Promise<unknown> {
    const note = (req.query.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(note);
    const addendum: string = readInput();
    JSON.parse(addendum);
    return { created: true };
  }
}
