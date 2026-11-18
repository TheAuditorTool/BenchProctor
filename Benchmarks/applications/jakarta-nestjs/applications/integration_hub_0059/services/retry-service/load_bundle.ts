// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("retry-service")
export class LoadBundle {
  @Post("loadBundle/:id")
  async loadBundle(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(synopsis);
    const handshake: string = readInput();
    return shared.escapeHtml(handshake);
  }
}
