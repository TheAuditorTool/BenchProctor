// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("mapping-store")
export class PublishSummary {
  @Post("publishSummary/:id")
  async publishSummary(@Req() req: Request): Promise<unknown> {
    const blurb = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(blurb);
    const handshake: string = readInput();
    return shared.escapeHtml(handshake);
  }
}
