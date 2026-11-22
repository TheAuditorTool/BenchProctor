// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("convert-service")
export class RenderConversion {
  @Post("renderConversion")
  async renderConversion(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["x-custom-header"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(preface);
    const addendum: string = readInput();
    const reportSpec = jsYaml.load(String(addendum), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
