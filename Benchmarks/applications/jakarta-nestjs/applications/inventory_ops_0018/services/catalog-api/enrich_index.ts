// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("catalog-api")
export class EnrichIndex {
  @Post("enrichIndex/:id")
  async enrichIndex(@Req() req: Request): Promise<unknown> {
    const transcript = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(transcript);
    const backorder: string = readInput();
    return shared.escapeHtml(backorder);
  }
}
