// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Redirect } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00152")
  @Redirect()
  async BenchmarkTest00152(): Promise<unknown> {
    const userInput = process.env.APP_INPUT || "";
    const data = String(userInput).replace(/\u0000/g, "");
    return { url: data };
  }
}
