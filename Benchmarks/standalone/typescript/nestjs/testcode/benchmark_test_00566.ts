// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Redirect, Req } from "@nestjs/common";
import { Request, Response } from "express";
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
  @Post("BenchmarkTest00566")
  @Redirect()
  async BenchmarkTest00566(@Req() req: Request): Promise<unknown> {
    const userInput = (req.body as string) || "";
    const data = Buffer.from(userInput, "utf-8").toString();
    return { url: data };
  }
}
