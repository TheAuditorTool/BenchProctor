// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("upload-gateway")
export class RenderCaption {
  @Post("renderCaption")
  async renderCaption(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers["x-custom-header"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(synopsis);
    const rendition: string = readInput();
    const reportSpec = jsYaml.load(String(rendition), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
