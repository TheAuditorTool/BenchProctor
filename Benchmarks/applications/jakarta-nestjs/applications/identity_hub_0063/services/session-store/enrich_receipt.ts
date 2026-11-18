// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("session-store")
export class EnrichReceipt {
  @Post("enrichReceipt/:id")
  async enrichReceipt(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(paragraph);
    const persona: string = readInput();
    return shared.escapeHtml(persona);
  }
}
