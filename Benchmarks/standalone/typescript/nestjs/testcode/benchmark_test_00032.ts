// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request, Response } from "express";
import * as libxmljs from "libxmljs";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00032")
  async BenchmarkTest00032(@Req() req: Request): Promise<unknown> {
    const userInput = ((req as any).rawBody as string) || "";
    const data = userInput != null ? userInput : '';
    libxmljs.parseXml(data, { noent: true, dtdload: true, nonet: false } as libxmljs.XMLParseOptions);
    return { created: true };
  }
}
