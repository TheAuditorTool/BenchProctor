// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("survey-service")
export class ValidateBundle {
  @Post("validateBundle/:id")
  async validateBundle(@Req() req: Request): Promise<unknown> {
    const phrase = (req.params.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(phrase);
    const inquiry: string = readInput();
    return shared.escapeHtml(inquiry);
  }
}
