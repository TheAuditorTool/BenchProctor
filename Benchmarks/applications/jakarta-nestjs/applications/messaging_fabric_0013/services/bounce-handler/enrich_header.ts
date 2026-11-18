// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("bounce-handler")
export class EnrichHeader {
  @Post("enrichHeader")
  async enrichHeader(@Req() req: Request): Promise<unknown> {
    const summary = (req.query.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(summary);
    const bulletin: string = readInput();
    JSON.parse(bulletin);
    return { created: true };
  }
}
