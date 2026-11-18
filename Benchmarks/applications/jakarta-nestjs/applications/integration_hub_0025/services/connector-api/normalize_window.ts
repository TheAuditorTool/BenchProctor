// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("connector-api")
export class NormalizeWindow {
  @Post("normalizeWindow/:id")
  async normalizeWindow(@Req() req: Request): Promise<unknown> {
    const footnote = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(footnote);
    const handshake: string = readInput();
    return shared.escapeHtml(handshake);
  }
}
